let isHidden = true;
let isHidden1 = true;
let loading = true;

const nameController = document.getElementById('fullName');
const mailController = document.getElementById('email');
const passwordController = document.getElementById('password');
const passwordConfirmationController = document.getElementById('passwordConfirmation');

function showToast(message) {
    // Create a toast element
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;

    // Append the toast to the body
    document.body.appendChild(toast);

    // Remove the toast after a certain duration
    setTimeout(() => {
        document.body.removeChild(toast);
    }, 3000); // Adjust the duration as needed
}

function validation(){
    if (nameController.value.trim() === '') {
        showToast('Please Enter your name');
        loading = true;
        return;
    }

    if (mailController.value.trim() === '') {
        showToast('Please Enter your email');
        loading = true;
        return;
    }

    const emailRegex = /^[a-zA-Z0-9.a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]+@[a-zA-Z0-9]+\.[a-zA-Z]+$/;
    if (!emailRegex.test(mailController.value.trim())) {
        showToast('Please Enter a valid email');
        loading = true;
        return;
    }

    const passwordRegex = /^[a-zA-Z0-9.a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]+@[a-zA-Z0-9]+\.[a-zA-Z]+$/;
    if (passwordController.value.trim() === '' || (!passwordRegex.test(passwordController.value.trim()) && passwordController.value.length < 8)) {
        showToast('Please Enter a strong password');
        loading = true;
        return;
    }

    if (passwordConfirmationController.value.trim() === '' || passwordConfirmationController.value.trim() !== passwordController.value.trim()) {
        showToast('Invalid password Confirmation');
        loading = true;

    } else {
        loading = false;
    }
}

function requestSignup(mail, name, password, permission) {
    const preLoginUrl = "https://driveguardian.ltn:8443/api/user";
    const data = {
        mail: mail,
        fullname: name,
        password: password,
        permissionLevel: permission
    };
    console.log("data : ", data);

    // Implement your AJAX request using fetch
    return fetch(preLoginUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            // Handle the response accordingly
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(responseData => {
            console.log('response : ', responseData);
            // Do something with the responseData if needed
        })
        .catch(error => {
            console.error('Error during signup: ', error);
        });
}

/*
function register() {
    validation();
    console.log(loading);

    try {
        requestSignup(mailController.value, nameController.value, passwordController.value, 1);
    } catch (error) {
        showToast('Invalid Signup');
        loading = true;
    }

    if (!loading) {
        // Implement navigation to the success page
        window.location.href = '/pages/registersuccess.html';
    }
}
*/

async function register() {
    validation();
    console.log(loading);

    try {
        await requestSignup(mailController.value, nameController.value, passwordController.value, 1);
        // If requestSignup is successful, navigate to the success page
        if (!loading) {
            window.location.href = 'signin.html';
        }
    } catch (error) {
        showToast('Invalid Signup');
        loading = true;
    }
}


function goToLogin() {
    // Implement navigation to the login page
    window.location.href = 'signin.html';
}
