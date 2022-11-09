<template>
    <div>
        <div v-if="!editable">
            <!-- <span class="border-rounded bg-dark">{{ book.title }}</span>
            <span>{{ book.author }}</span>
            <span>{{ book.publisher }}</span>
            <span>{{ book.stock }}</span>
            <button>Edit</button> -->
            <div class="container p-2">
                <div class="row">
                    <div class="col-sm-3 border rounded border-primary p-2">
                        <p class="">{{ edited.title }}</p>
                    </div>
                    <div class="col-sm-3 border rounded border-primary p-2">
                        {{ edited.author }}
                    </div>
                    <div class="col-sm-3 border rounded border-primary p-2">
                        {{ edited.publisher }}
                    </div>
                    <div class="col-sm-3 border rounded border-primary p-2">
                        {{ edited.stock }}
                    </div>
                </div>
                <button class="mt-3 btn btn-primary active" @click="setEditable">Edit</button>
            </div>
        </div>
        <div v-else>
            <form @submit="updateBook" class="container">
                <input class="col-sm col-sm border rounded border-primary p-2" name="title" type="text"
                    v-model="edited.title">
                <input class="col-sm col-sm border rounded border-primary p-2" name="author" type="text"
                    v-model="edited.author">
                <input class="col-sm col-sm border rounded border-primary p-2" name="publisher" type="text"
                    v-model="edited.publisher">
                <input class="col-sm col-sm border rounded border-primary p-2" name="stock" type="text"
                    v-model="edited.stock">
                <input class="col-sm col-sm border rounded border-primary p-2" type="submit" value="Submit">
            </form>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        book: {
            type: Object
        },
        // updateBook: {
        //     type: Function
        // }
    },

    data() {
        return {
            editable: false,
            edited: {
                title: this.book.title,
                author: this.book.author,
                publisher: this.book.publisher,
                stock: this.book.stock,
            }
        }
    },

    methods: {
        setEditable() {
            this.editable = !this.editable
        },

        // editBook(e) {
        //     this.updateBook(e, edited)
        //     this.setEditable()
        // },

        async updateBook(e) {
            e.preventDefault()
            console.log("HERE")
            fetch("http://localhost:8000/api/books/", {
                method: "PUT",
                body: JSON.stringify({
                    id: this.book.id,
                    title: this.edited.title,
                    author: this.edited.author,
                    publisher: this.edited.publisher,
                    stock: this.edited.stock
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
            this.setEditable()
        },

        // deleteBook() {
        //     this.deleteBook(book)
        // }
    }
}
</script>