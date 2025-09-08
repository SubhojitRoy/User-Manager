
<template>
  <div class="row g-4">
    <div class="col-12 col-lg-8">
      <div class="card p-3">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h5 class="mb-0">Users</h5>
          <div class="d-flex gap-2">
            <input v-model="q" class="form-control form-control-sm" placeholder="Search..." style="min-width:200px" />
            <button class="btn btn-sm btn-outline-secondary" @click="load">Refresh</button>
          </div>
        </div>
        <div class="table-responsive">
          <table class="table table-hover table-striped align-middle">
            <thead class="table-light">
              <tr><th>ID</th><th>Username</th><th>Attribute</th><th>Op</th><th>Value</th><th>Actions</th></tr>
            </thead>
            <tbody>
              <tr v-for="u in filtered" :key="u.id">
                <td>{{ u.id }}</td>
                <td>{{ u.username }}</td>
                <td><span class="badge bg-secondary">{{ u.attribute }}</span></td>
                <td><span class="badge bg-info text-dark">{{ u.op }}</span></td>
                <td>{{ u.value }}</td>
                <td style="white-space:nowrap">
                  <button class="btn btn-sm btn-primary me-2" @click="startEdit(u)">Edit</button>
                  <button class="btn btn-sm btn-danger" @click="remove(u.id)">Delete</button>
                </td>
              </tr>
              <tr v-if="!filtered.length"><td colspan="6" class="text-muted">No data</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="col-12 col-lg-4">
      <div class="card p-3 mb-3">
        <h6>New User</h6>
        <div class="row mt-2">
          <div class="col-md-12 mb-3"><label class="form-label">Username</label><input class="form-control" v-model="form.username" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Password</label><input class="form-control" v-model="form.password" type="text" /></div>
        </div>
        <div class="d-flex justify-content-end"><button class="btn btn-success" @click="createItem">Create</button></div>
      </div>
      <div v-if="editing" class="card p-3">
        <h6>Edit #{{ editing.id }}</h6>
        <div class="row">
          <div class="col-md-12 mb-3"><label class="form-label">Username</label><input class="form-control" v-model="editing.username" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Password (leave empty to keep)</label><input class="form-control" v-model="editing.password" type="text" /></div>
        </div>
        <div class="d-flex gap-2 justify-content-end">
          <button class="btn btn-primary" @click="saveEdit">Save</button>
          <button class="btn btn-secondary" @click="editing=null">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '../api'
const items = ref([])
const q = ref('')
const form = ref({ username: '', password: '' })
const editing = ref(null)
const filtered = computed(() => {
  if (!q.value) return items.value
  const t = q.value.toLowerCase()
  return items.value.filter(i => String(i.username).toLowerCase().includes(t))
})
async function load() {
  try {
    const res = await api.get('/user')
    items.value = res.data
  } catch (e) {
    console.error(e)
    alert('Failed to load users. Check API base URL and CORS.')
  }
}
async function createItem() {
  try {
    if (!form.value.username || !form.value.password) return alert('username & password required')
    await api.post('/user', form.value)
    form.value = { username: '', password: '' }
    await load()
  } catch (e) {
    console.error(e)
    alert('Create failed: ' + (e.response?.data?.error || e.message))
  }
}
function startEdit(u) { editing.value = { id: u.id, username: u.username, password: '' } }
async function saveEdit() {
  try {
    const payload = { username: editing.value.username }
    if (editing.value.password) payload.password = editing.value.password
    await api.put(`/user/${editing.value.id}`, payload)
    editing.value = null
    await load()
  } catch (e) {
    console.error(e)
    alert('Update failed: ' + (e.response?.data?.error || e.message))
  }
}
async function remove(id) {
  if (!confirm('Delete user #' + id + '?')) return
  try {
    await api.delete(`/user/${id}`)
    await load()
  } catch (e) {
    console.error(e)
    alert('Delete failed: ' + (e.response?.data?.error || e.message))
  }
}
onMounted(load)
</script>
