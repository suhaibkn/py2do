var app = new Vue({
    el: '.main',
    data() {
        return {
            todos: null,
            loading: false,
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:5000/api/get/active').then(response => (this.todos = response.data))
    }
});