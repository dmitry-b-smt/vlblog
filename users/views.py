from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, ProfileImageForm, UpdateForm, EditPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from random import choice, sample, shuffle



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно зарегистрирован')
            return redirect('home')
    else:

        password = []
        counter_n = 0
        counter_l = 0
        counter_u = 0
        counter_s = 0

        def numbers():
            num_lst = [int(i) for i in range(0, 10, 1)]
            num = str(choice(num_lst))
            return num

        def lower_alpha():
            low_alph_lst = [str(chr(i)) for i in range(97, 123)]
            lowa = choice(low_alph_lst)
            return lowa

        def upper_alpha():
            upp_alph_lst = [str(chr(i)) for i in range(65, 90)]
            uppa = choice(upp_alph_lst)
            return uppa

        def special_sym():
            spec = [str(chr(i)) for i in range(33, 43)]
            cpsym = choice(spec)
            return cpsym

        def generate_password():
            for i in range(1, 9, 1):
                password.append(str(numbers()))
                password.append(lower_alpha())
                password.append(upper_alpha())
                password.append(special_sym())

            shuffle(password)
            result = sample(password, 8)
            return result

        while counter_n < 1 or counter_l < 1 or counter_u < 1 or counter_s < 1:
            counter_n = 0
            counter_l = 0
            counter_u = 0
            counter_s = 0
            generate_password()
            password = generate_password()
            for i in password:
                if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    counter_n += 1
                    continue
                if i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']:
                    counter_l += 1
                    continue
                if i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y']:
                    counter_u += 1
                    continue
                if i in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*']:
                    counter_s += 1
                    continue
            if counter_n >= 1 and counter_l >= 1 and counter_u >= 1 and counter_s >= 1:
                password = ''.join(password)
                break

        form = RegistrationForm()
        data = {
             'title': 'Страница регистрации',
             'form': form,
             'password': password,
            }
        return render(request, 'users/registration.html', data)


@login_required
def profile(request):
    if request.method == 'POST':
        profileimageForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateForm = UpdateForm(request.POST, instance=request.user)

        if profileimageForm.is_valid() and updateForm.is_valid():
            profileimageForm.save()
            updateForm.save()
            username = updateForm.cleaned_data.get('username')
            messages.success(request, f'Профиль {username} был успешно обновлён')
            return redirect('profile')

    else:
        profileimageForm = ProfileImageForm(instance=request.user.profile)
        updateForm = UpdateForm(instance=request.user)

    data = {
        'profileimageForm': profileimageForm,
        'updateForm': updateForm,
    }
    return render(request, 'users/profile.html', data)

@login_required
def change_password(request):

    if request.method == 'POST':
        form = EditPasswordForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, f'Пароль пользователя {request.user} был успешно обновлён')
            return redirect('profile')

    else:

        password = []
        counter_n = 0
        counter_l = 0
        counter_u = 0
        counter_s = 0

        def numbers():
            num_lst = [int(i) for i in range(0, 10, 1)]
            num = str(choice(num_lst))
            return num

        def lower_alpha():
            low_alph_lst = [str(chr(i)) for i in range(97, 123)]
            lowa = choice(low_alph_lst)
            return lowa

        def upper_alpha():
            upp_alph_lst = [str(chr(i)) for i in range(65, 90)]
            uppa = choice(upp_alph_lst)
            return uppa

        def special_sym():
            spec = [str(chr(i)) for i in range(33, 43)]
            cpsym = choice(spec)
            return cpsym

        def generate_password():
            for i in range(1, 9, 1):
                password.append(str(numbers()))
                password.append(lower_alpha())
                password.append(upper_alpha())
                password.append(special_sym())

            shuffle(password)
            result = sample(password, 8)
            return result

        while counter_n < 1 or counter_l < 1 or counter_u < 1 or counter_s < 1:
            counter_n = 0
            counter_l = 0
            counter_u = 0
            counter_s = 0
            generate_password()
            password = generate_password()
            for i in password:
                if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    counter_n += 1
                    continue
                if i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                    counter_l += 1
                    continue
                if i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']:
                    counter_u += 1
                    continue
                if i in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*']:
                    counter_s += 1
                    continue
            if counter_n >= 1 and counter_l >= 1 and counter_u >= 1 and counter_s >= 1:
                password = ''.join(password)
                break

        form = EditPasswordForm(user=request.user)
        args = {
                'form': form, 'password': password
               }

        return render(request, 'users/change_password.html', args)