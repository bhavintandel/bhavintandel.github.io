Title: Contact
Date: 2024-05-08 22:17
Modified: 2024-06-13 19:13
Slug: contact
Summary: Contact details.

Feel free to reach out with any questions, comments, or inquiries.

### Contact Information

<div class="col-md-12">
    <form id="contactForm" class="gform" method="POST">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" class="form-control" placeholder="Your Name" required>
        </div>
        <div class="form-group">
            <label for="subject">Subject:</label>
            <input type="text" id="subject" name="subject" class="form-control" placeholder="Subject">
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" class="form-control" placeholder="Your Email" required>
        </div>
        <div class="form-group">
            <label for="message">Message:</label>
            <textarea id="message" name="message" class="form-control" placeholder="Your Message" rows="4" required></textarea>
        </div>
        <!-- Honeypot field (hidden from users) -->
        <input type="text" name="honeypot" style="display: none;">
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>

<style>
    .form-group {
        margin-bottom: 15px;
    }

    .form-control {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .btn-primary {
        background-color: #007bff;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        color: #fff;
        cursor: pointer;
    }

    .btn-primary:hover {
        background-color: #0056b3;
    }
</style>

<script>
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(this);
        const actionUrl = 'https://script.google.com/macros/s/AKfycbwMhjMZOsmUHmjgnFaD2DqWaIfjMC9X8NOOZ70jJ4abrKZBvW9vbRrzkm-dJr_x8C5p/exec';

        fetch(actionUrl, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.result === 'success') {
                alert('Form submitted successfully!');
                this.reset(); // Reset the form
            } else {
                console.error('Form submission error:', data);
                alert('Form submission failed. Please try again.');
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            alert('An error occurred. Please try again.');
        });
    });
</script>

### Address

Earth 🌍

### Social Media

Connect with us on social media for updates, news, and more:

- **Twitter:** [@Big_Bhavin](https://twitter.com/Big_Bhavin)
- **LinkedIn:** [@bhavintandel](https://www.linkedin.com/in/bhavintandel/)
