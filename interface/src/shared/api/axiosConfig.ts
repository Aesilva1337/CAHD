import axios from 'axios';

export default axios.create({
  baseURL: 'http://localhost:44390/api'  
});