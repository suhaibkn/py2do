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
            event.preventDefault();
            let todo_data = {
                todo: document.getElementById('new-todo').value,
                created_at: (new Date()).toISOString()
            };

            this.todos.push(todo_data);
            document.getElementById('new-todo').value = '';

            axios
                .post('http://127.0.0.1:5000/api/new', todo_data)
                .then(function (response) {
                    console.log(response);
                    this.todos = response.data
                })
                .catch(function (error) {
                    console.log(error);
                });

        },
        refreshData: function (event) {
            this.loading = true;
            this.todos = [];
            axios
                .get('http://127.0.0.1:5000/api/get/active')
                .then(response => (this.todos = response.data))
                .finally(() => {
                    this.loading = false
                })
        }
    },
    mounted() {
        this.refreshData()
    },
});