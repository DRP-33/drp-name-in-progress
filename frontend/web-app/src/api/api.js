import axios from 'axios'

const instance = axios.create({
    baseURL: 'https://drp-33.herokuapp.com',
    headers: {}
});

const api = {
    getTask: () =>
    instance({
        'method':'GET',
        'url': '/tasks'
    }),
    acceptTask: (key) =>
    instance({
        'method': 'POST',
        'url': '/task_a',
        'data': {
            'id': 'key'
        }
    })
}

export default api;