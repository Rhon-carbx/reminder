 document.addEventListener('DOMContentLoaded', function() {
        const sidebar = document.querySelector('.sidebar');
        const btn = document.getElementById('btn');
        btn.addEventListener('click', function() {
          sidebar.classList.toggle('active');
          // Adjust main margin
          document.querySelector('main').classList.toggle('active');
        });
      });