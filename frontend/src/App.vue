<template>
  <div class="h-100 d-flex align-items-center justify-content-center">
    <div class="d-flex flex-column p-2">
      <div>
        <button v-if="!showBooks" @click="fetchBooks">View Books</button>
        <button v-else @click="toggleShowBooks">Hide Books</button>
        <div v-show="showBooks">
          <div class="container">
            <div class="row">
              <div class="h4 col-sm border rounded border-primary p-2">
                Title
              </div>
              <div class="h4 col-sm border rounded border-primary p-2">
                Author
              </div>
              <div class="h4 col-sm border rounded border-primary p-2">
                Publisher
              </div>
              <div class="h4 col-sm border rounded border-primary p-2">
                Stock
              </div>
            </div>
          </div>
          <div v-for="book in books">
            <BookVue :book="book" />
          </div>
        </div>
      </div>
      <div>
        <button v-show="!showAddBook" @click="addBook">Add books</button>
        <form @submit="addBook">
          Title
          <input name="title" type="text" v-model="form.title">
          Author
          <input name="author" type="text" v-model="form.author">
          Publisher
          <input name="publisher" v-model="form.publisher">
          Stock
          <input name="stock" type="text" v-model="form.stock">
          <input type="submit" value="Submit">
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import BookVue from './components/Book.vue'

export default {
  components: {
    BookVue
  },
  data() {
    return {
      showBooks: false,
      showAddBook: false,
      books: [],
      form: {
        title: '',
        author: '',
        publisher: '',
        stock: '',
      }
    }
  },
  methods: {
    async fetchBooks() {
      const response = await fetch("http://localhost:8000/api/books/")
      const data = await response.json()
      this.books = data.books
      this.toggleShowBooks()
    },

    toggleShowBooks() {
      this.showBooks = !this.showBooks
    },

    toggleShowAddBook() {
      this.showAddBook = !this.showAddBook
    },

    // changeState(state) {
    //   state = !state
    // },

    async addBook(e) {
      e.preventDefault()
      fetch("http://localhost:8000/api/books/", {
        method: "POST",
        body: JSON.stringify({
          title: this.form.title,
          author: this.form.author,
          publisher: this.form.publisher,
          stock: this.form.stock,
        })
      })
        .then((response) => {
          return response
        })
        .then((data) => {
          console.log("SUCCESS")
          console.log(data)
        })
        .catch((error) => {
          console.log("ERROR")
          console.log(error)
        })
    },
  }
}
</script>
