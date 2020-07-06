<template>
    <div>
        <div class="container center-block mt-4"
             v-for="recipe in recipes"
             :key="recipe.id"
        >
            <div class="card mb-3 card-background">
                <h3 class="card-header">{{ recipe.title }}</h3>
                <ul class="list-group list-group-flush card-background">
                    <li class="list-group-item card-background">
                        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-clock mr-1" fill="currentColor"
                             xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                  d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm8-7A8 8 0 1 1 0 8a8 8 0 0 1 16 0z"/>
                            <path fill-rule="evenodd"
                                  d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5z"/>
                        </svg>
                        {{ recipe.prep_time }} minutes
                    </li>
                </ul>
                <img :src="recipe.image" alt=""/>
                <ul class="list-group list-group-flush card-background">
                    <li class="list-group-item card-background">
                        {{ recipe.ingredients }}
                    </li>
                </ul>
                <div class="card-body">
                    <p class="card-text"> {{ recipe.description }}</p>
                </div>

                <div class="card-body">
                    <a href="#" class="card-link">Card link</a>
                    <a href="#" class="card-link">Another link</a>
                </div>
                <div class="card-footer text-muted">
                    Created: {{ recipe.created_at|formatDate }}
                    <div>
                        Updated: {{ recipe.updated_at|formatDate }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {apiService} from "../common/api.service";
    import moment from "moment";

    export default {
        name: "Recipe",
        data() {
            return {
                loadingRecipes: false,
                recipes: []
            }
        },
        methods: {
            getRecipes() {
                let endpoint = '/api/recipes/';
                if (this.next) {
                    endpoint = this.next;
                }
                this.loadingRecipes = true;
                apiService(endpoint)
                    .then(data => {
                        this.recipes.push(...data.results);
                        this.loadingRecipes = false;
                        if (data.next) {
                            this.next = data.next;
                        } else {
                            this.next = null;
                        }
                    })
            },
        },
        created() {
            this.getRecipes()
        },
        filters: {
            formatDate: function (value) {
                if (value) {
                    return moment(String(value)).format('DD/MM/YYYY hh:mm')
                }
            }
        }
    }
</script>

<style scoped>
    .card-background {
        background-color: #333a41;
    }

</style>