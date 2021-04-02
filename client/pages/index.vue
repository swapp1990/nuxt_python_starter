<template>
	<div>
		Starter Page
	</div>
</template>

<script>
	export default {
		created() {
			// this.socket = this.$nuxtSocket({ channel: "/" });
			fetch(process.env.SERVER_URL+"/ping")
				.then(result => console.log(result));
		}
	}
</script>

<style lang="scss" scoped>

</style>