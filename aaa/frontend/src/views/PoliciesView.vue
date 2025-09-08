
<template>
  <div class="row g-4">
    <div class="col-12 col-lg-8">
      <div class="card p-3">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h5 class="mb-0">User Policies</h5>
          <div class="d-flex gap-2">
            <input v-model="q" class="form-control form-control-sm" placeholder="Search..." style="min-width:200px" />
            <button class="btn btn-sm btn-outline-secondary" @click="load">Refresh</button>
          </div>
        </div>
        <div class="table-responsive">
          <table class="table table-hover table-striped align-middle">
            <thead class="table-light"><tr><th>ID</th><th>Username</th><th>NAS IP</th><th>Mikrotik Group</th><th>Actions</th></tr></thead>
            <tbody>
              <tr v-for="p in filtered" :key="p.id">
                <td>{{ p.id }}</td><td>{{ p.username }}</td><td>{{ p.nas_ip }}</td><td>{{ p.mikrotik_group }}</td>
                <td style="white-space:nowrap"><button class="btn btn-sm btn-primary me-2" @click="startEdit(p)">Edit</button><button class="btn btn-sm btn-danger" @click="remove(p.id)">Delete</button></td>
              </tr>
              <tr v-if="!filtered.length"><td colspan="5" class="text-muted">No data</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="col-12 col-lg-4">
      <div class="card p-3 mb-3">
        <h6>New Policy</h6>
        <div class="row mt-2">
          <div class="col-md-12 mb-3"><label class="form-label">Username</label><input class="form-control" v-model="form.username" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">NAS IP</label><input class="form-control" v-model="form.nas_ip" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Mikrotik Group</label><input class="form-control" v-model="form.mikrotik_group" /></div>
        </div>
        <div class="d-flex justify-content-end"><button class="btn btn-success" @click="createItem">Create</button></div>
      </div>
      <div v-if="editing" class="card p-3">
        <h6>Edit #{{ editing.id }}</h6>
        <div class="row">
          <div class="col-md-12 mb-3"><label class="form-label">Username</label><input class="form-control" v-model="editing.username" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">NAS IP</label><input class="form-control" v-model="editing.nas_ip" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Mikrotik Group</label><input class="form-control" v-model="editing.mikrotik_group" /></div>
        </div>
        <div class="d-flex gap-2 justify-content-end"><button class="btn btn-primary" @click="saveEdit">Save</button><button class="btn btn-secondary" @click="editing=null">Cancel</button></div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '../api'
const items = ref([]); const q = ref(''); const form = ref({ username:'', nas_ip:'', mikrotik_group:'' }); const editing = ref(null)
const filtered = computed(()=>{ if(!q.value) return items.value; const t=q.value.toLowerCase(); return items.value.filter(i=>Object.values(i).some(v=>String(v).toLowerCase().includes(t))) })
async function load(){ try{ const res=await api.get('/policy'); items.value=res.data }catch(e){console.error(e);alert('Failed to load policies. Check API base URL and CORS.')} }
async function createItem(){ try{ if(!form.value.username||!form.value.nas_ip||!form.value.mikrotik_group) return alert('username,nas_ip,mikrotik_group required'); await api.post('/policy', form.value); form.value={username:'',nas_ip:'',mikrotik_group:''}; await load() }catch(e){console.error(e);alert('Create failed: '+(e.response?.data?.error||e.message))} }
function startEdit(u){ editing.value={...u} }
async function saveEdit(){ try{ await api.put(`/policy/${editing.value.id}`, editing.value); editing.value=null; await load() }catch(e){console.error(e);alert('Update failed: '+(e.response?.data?.error||e.message))} }
async function remove(id){ if(!confirm('Delete policy #'+id+'?'))return; try{ await api.delete(`/policy/${id}`); await load() }catch(e){console.error(e);alert('Delete failed: '+(e.response?.data?.error||e.message))} }
onMounted(load)
</script>
