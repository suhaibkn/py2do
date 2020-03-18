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
                .get('http://127.0.0.1:5000/api/get/all')
                .then(response => (this.todos = response.data))
                .finally(() => {
                    this.loading = false
                })
        },
        cleanData: function (event) {
            this.loading = true;
            this.todos = [];
            axios
                .delete('http://127.0.0.1:5000/api/clean')
                .then(response => (this.todos = response.data))
                .finally(() => {
                    this.loading = false
                })
        },
        toggleStatus: function (item) {
            this.loading = true;
            console.log(item.id)
            axios
                .get('http://127.0.0.1:5000/api/toggledone/'+item.id)
                .then(response => (this.todos = response.data))
                .finally(() => {
                    this.loading = false
                })
        },
        newFocus: function (item) {
            document.getElementById('new-todo').focus();
        },
    },
    mounted() {
        this.refreshData()
    },
    computed: {
        count: function () {
            return this.todos.length
        },
        available: function () {
            return (this.count > 0)
        }
    }
});