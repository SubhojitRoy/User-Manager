
<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="#">RADIUS Admin</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMenu"><span class="navbar-toggler-icon"></span></button>
        <div class="collapse navbar-collapse" id="navMenu">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><RouterLink class="nav-link" to="/">Users</RouterLink></li>
            <li class="nav-item"><RouterLink class="nav-link" to="/groups">Groups</RouterLink></li>
            <li class="nav-item"><RouterLink class="nav-link" to="/nas">NAS Devices</RouterLink></li>
            <li class="nav-item"><RouterLink class="nav-link" to="/policies">Policies</RouterLink></li>
          </ul>
        </div>
      </div>
    </nav>
    <main class="container my-4">
      <RouterView />
      <footer class="text-center text-muted mt-5">RADIUS Admin</footer>
    </main>
  </div>
</template>
<script setup></script>
