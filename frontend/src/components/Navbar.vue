<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <router-link
                :to="{ name: 'Home'}"
                class="navbar-brand"
                style="text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;"
        >
            Advanced Planner
        </router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor02"
                aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarColor02">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <router-link
                            :to="{ name: 'Todolist' }"
                            class="nav-link"
                    >To-do list
                    </router-link>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Recipes</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Shopping list</a>
                </li>
            </ul>
            <button class="btn btn-secondary my-2 my-sm-0" style="margin-right: 10px">My Profile</button>
            <button class="btn btn-secondary my-2 my-sm-0" type="submit">Logout</button>
        </div>
    </nav>
</template>

<script>
    export default {
        name: "Navbar"
    }
</script>

<style scoped>

</style>