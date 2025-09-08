
<template>
  <div class="row g-4">
    <div class="col-12 col-lg-8">
      <div class="card p-3">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h5 class="mb-0">Groups</h5>
          <div class="d-flex gap-2">
            <input v-model="q" class="form-control form-control-sm" placeholder="Search..." style="min-width:200px" />
            <button class="btn btn-sm btn-outline-secondary" @click="load">Refresh</button>
          </div>
        </div>
        <div class="table-responsive">
          <table class="table table-hover table-striped align-middle">
            <thead class="table-light"><tr><th>ID</th><th>Group Name</th><th>Attribute</th><th>Op</th><th>Value</th><th>Actions</th></tr></thead>
            <tbody>
              <tr v-for="g in filtered" :key="g.id">
                <td>{{ g.id }}</td><td>{{ g.groupname }}</td><td>{{ g.attribute }}</td><td>{{ g.op }}</td><td>{{ g.value }}</td>
                <td style="white-space:nowrap"><button class="btn btn-sm btn-primary me-2" @click="startEdit(g)">Edit</button><button class="btn btn-sm btn-danger" @click="remove(g.id)">Delete</button></td>
              </tr>
              <tr v-if="!filtered.length"><td colspan="6" class="text-muted">No data</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="col-12 col-lg-4">
      <div class="card p-3 mb-3">
        <h6>New Group</h6>
        <div class="row mt-2">
          <div class="col-md-12 mb-3"><label class="form-label">Group Name</label><input class="form-control" v-model="form.groupname" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Attribute</label><input class="form-control" v-model="form.attribute" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Op</label><input class="form-control" v-model="form.op" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Value</label><input class="form-control" v-model="form.value" /></div>
        </div>
        <div class="d-flex justify-content-end"><button class="btn btn-success" @click="createItem">Create</button></div>
      </div>
      <div v-if="editing" class="card p-3">
        <h6>Edit #{{ editing.id }}</h6>
        <div class="row">
          <div class="col-md-12 mb-3"><label class="form-label">Group Name</label><input class="form-control" v-model="editing.groupname" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Attribute</label><input class="form-control" v-model="editing.attribute" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Op</label><input class="form-control" v-model="editing.op" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Value</label><input class="form-control" v-model="editing.value" /></div>
        </div>
        <div class="d-flex gap-2 justify-content-end"><button class="btn btn-primary" @click="saveEdit">Save</button><button class="btn btn-secondary" @click="editing=null">Cancel</button></div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '../api'
const items = ref([]); const q = ref(''); const form = ref({ groupname: '', attribute:'', op:'', value:'' }); const editing = ref(null)
const filtered = computed(()=>{ if (!q.value) return items.value; const t=q.value.toLowerCase(); return items.value.filter(i=>Object.values(i).some(v=>String(v).toLowerCase().includes(t))) })
async function load(){ try{ const res=await api.get('/group'); items.value=res.data }catch(e){console.error(e);alert('Failed to load groups. Check API base URL and CORS.')} }
async function createItem(){ try{ if(!form.value.groupname) return alert('groupname required'); await api.post('/group', form.value); form.value={groupname:'',attribute:'',op:'',value:''}; await load() }catch(e){console.error(e);alert('Create failed: '+(e.response?.data?.error||e.message))} }
function startEdit(u){ editing.value={...u} }
async function saveEdit(){ try{ await api.put(`/group/${editing.value.id}`, editing.value); editing.value=null; await load() }catch(e){console.error(e);alert('Update failed: '+(e.response?.data?.error||e.message))} }
async function remove(id){ if(!confirm('Delete group #'+id+'?'))return; try{ await api.delete(`/group/${id}`); await load() }catch(e){console.error(e);alert('Delete failed: '+(e.response?.data?.error||e.message))} }
onMounted(load)
</script>
