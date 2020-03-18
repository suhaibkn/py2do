var app = new Vue({
    el: '#app',
    data() {
        return {
            todos: [],
            loading: false,
        }
    },
    methods: {
        newTodo: function (event) {
            event.preventDefault()
            let val = {
                todo: document.getElementById('new-todo').value,
            }
            this.todos.push(val)
            document.getElementById('new-todo').value = ''
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:5000/api/get/active').then(response => (this.todos = response.data))
    },
});