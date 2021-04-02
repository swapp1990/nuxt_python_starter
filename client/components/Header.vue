<template>
	<div class="bg-white myheader">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div
        class="flex justify-between items-center border-b-2 border-gray-100 md:justify-start md:space-x-10"
      >
        <div class="flex justify-start lg:w-0 lg:flex-1">
          <div
            class="p-1 text-md md:text-4xl antialiased font-bold cursor-pointer"
            @click="goHome()"
          >
            <h1>Starter Project</h1>
          </div>
        </div>
        <nav class="hidden md:flex space-x-10"></nav>
        <div class="md:flex items-center justify-end md:flex-1 lg:w-0">
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
	export default {
		
	}
</script>

<style lang="scss" scoped>
.myheader {
  font-family: "Inconsolata", monospace;
  width: 100%;
  top: 0%;
  left: 0%;
  position: fixed;
  z-index: 100;
}
</style>