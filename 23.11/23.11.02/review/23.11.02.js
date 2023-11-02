const { createApp, ref, computed } = Vue

const app = createApp({
    // setup(): 앱이 생성될 때 호출되는 메서드
    setup() {
        const todos = ref([])
        const newTodo = ref('')

        let todoId = 1;

        const addTodo = () => {
            tmp = {
                id: todoId++,
                text: newTodo.value,
                completed: false
            }
            todos.value.push(tmp)
            newTodo.value = ''
        }

        const deleteTodo = (index) => {
            todos.value.splice(index, 1)
        }

        const toggleTodoStatus = (todo) => {
            todo.completed = !todo.completed
        }

        const deleteCompletedTodos = () => {
            // todos.value = todos.value.filter((todo) => !todo.completed)
            todos.value = todos.value.filter((todo) => {
                return !todo.completed            
            })
        }

        // computed: 계산된 속성
        // 기존 변수를 수정하지 않고, 계산된 값만 가지고 새로운 변수를 만들고 싶을 때
        // computed 메서드 내에서 사용하는 변수가 변경이 생길 때 마다 새로 계산
        // 아래 예시에서는 todos 변수가 변경되면 바로 계산
        const todoCount = computed(() => {
            return todos.value.filter((todo) => todo.completed).length > 0
        })

        return {
            todos,
            newTodo,
            addTodo,
            deleteTodo,
            toggleTodoStatus,
            deleteCompletedTodos,
            todoCount
        }
    }
})

app.mount('#app')