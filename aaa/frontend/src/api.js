
import axios from 'axios'
const baseURL = import.meta.env.VITE_API_BASE_URL || 'http://10.50.1.6:5000'
const api = axios.create({ baseURL })
export default api
