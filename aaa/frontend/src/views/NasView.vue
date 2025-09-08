
<template>
  <div class="row g-4">
    <div class="col-12 col-lg-8">
      <div class="card p-3">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h5 class="mb-0">NAS Devices</h5>
          <div class="d-flex gap-2">
            <input v-model="q" class="form-control form-control-sm" placeholder="Search..." style="min-width:200px" />
            <button class="btn btn-sm btn-outline-secondary" @click="load">Refresh</button>
          </div>
        </div>
        <div class="table-responsive">
          <table class="table table-hover table-striped align-middle">
            <thead class="table-light"><tr><th>ID</th><th>NAS Name</th><th>Short Name</th><th>Type</th><th>Ports</th><th>Secret</th><th>Server</th><th>Community</th><th>Description</th><th>Actions</th></tr></thead>
            <tbody>
              <tr v-for="n in filtered" :key="n.id">
                <td>{{ n.id }}</td><td>{{ n.nasname }}</td><td>{{ n.shortname }}</td><td>{{ n.type }}</td><td>{{ n.ports }}</td><td>{{ n.secret }}</td><td>{{ n.server }}</td><td>{{ n.community }}</td><td>{{ n.description }}</td>
                <td style="white-space:nowrap"><button class="btn btn-sm btn-primary me-2" @click="startEdit(n)">Edit</button><button class="btn btn-sm btn-danger" @click="remove(n.id)">Delete</button></td>
              </tr>
              <tr v-if="!filtered.length"><td colspan="10" class="text-muted">No data</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="col-12 col-lg-4">
      <div class="card p-3 mb-3">
        <h6>New NAS</h6>
        <div class="row mt-2">
          <div class="col-md-12 mb-3"><label class="form-label">NAS Name</label><input class="form-control" v-model="form.nasname" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Short Name</label><input class="form-control" v-model="form.shortname" /></div>
          <div class="col-md-6 mb-3"><label class="form-label">Type</label><input class="form-control" v-model="form.type" /></div>
          <div class="col-md-6 mb-3"><label class="form-label">Ports</label><input class="form-control" v-model.number="form.ports" type="number" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Secret</label><input class="form-control" v-model="form.secret" type="text" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Server</label><input class="form-control" v-model="form.server" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Community</label><input class="form-control" v-model="form.community" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Description</label><textarea class="form-control" v-model="form.description" rows="2"></textarea></div>
        </div>
        <div class="d-flex justify-content-end"><button class="btn btn-success" @click="createItem">Create</button></div>
      </div>
      <div v-if="editing" class="card p-3">
        <h6>Edit #{{ editing.id }}</h6>
        <div class="row">
          <div class="col-md-12 mb-3"><label class="form-label">NAS Name</label><input class="form-control" v-model="editing.nasname" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Short Name</label><input class="form-control" v-model="editing.shortname" /></div>
          <div class="col-md-6 mb-3"><label class="form-label">Type</label><input class="form-control" v-model="editing.type" /></div>
          <div class="col-md-6 mb-3"><label class="form-label">Ports</label><input class="form-control" v-model.number="editing.ports" type="number" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Secret</label><input class="form-control" v-model="editing.secret" type="text" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Server</label><input class="form-control" v-model="editing.server" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Community</label><input class="form-control" v-model="editing.community" /></div>
          <div class="col-md-12 mb-3"><label class="form-label">Description</label><textarea class="form-control" v-model="editing.description" rows="2"></textarea></div>
        </div>
        <div class="d-flex gap-2 justify-content-end"><button class="btn btn-primary" @click="saveEdit">Save</button><button class="btn btn-secondary" @click="editing=null">Cancel</button></div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '../api'
const items = ref([]); const q = ref(''); const form = ref({ nasname:'', shortname:'', type:'', ports:null, secret:'', server:'', community:'', description:'' }); const editing = ref(null)
const filtered = computed(()=>{ if(!q.value) return items.value; const t=q.value.toLowerCase(); return items.value.filter(i=>Object.values(i).some(v=>String(v).toLowerCase().includes(t))) })
async function load(){ try{ const res=await api.get('/nas'); items.value=res.data }catch(e){console.error(e);alert('Failed to load NAS. Check API base URL and CORS.')} }
async function createItem(){ try{ if(!form.value.nasname) return alert('nasname required'); await api.post('/nas', form.value); form.value={nasname:'',shortname:'',type:'',ports:null,secret:'',server:'',community:'',description:''}; await load() }catch(e){console.error(e);alert('Create failed: '+(e.response?.data?.error||e.message))} }
function startEdit(u){ editing.value={...u} }
async function saveEdit(){ try{ await api.put(`/nas/${editing.value.id}`, editing.value); editing.value=null; await load() }catch(e){console.error(e);alert('Update failed: '+(e.response?.data?.error||e.message))} }
async function remove(id){ if(!confirm('Delete nas #'+id+'?'))return; try{ await api.delete(`/nas/${id}`); await load() }catch(e){console.error(e);alert('Delete failed: '+(e.response?.data?.error||e.message))} }
onMounted(load)
</script>
