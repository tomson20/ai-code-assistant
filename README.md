# AI Code Agent

AI პროგრამისტის აგენტი, რომელიც წერს კოდს, აქმნის ტესტებს, დოკუმენტაციას და ავტომატურად განთავსებს GitHub-ზე.

## დამოკიდებულებები
- Flask
- gunicorn
- PyGithub
- pytest
- pylint

## გაშვება Render-ში
1. შექმენით GitHub რეპოზიტორია
2. დაამატეთ `Procfile`: `web: gunicorn main:app`
3. დაამატეთ `requirements.txt`
4. დააინტეგრირეთ Render-ში
5. გამოიყენეთ როგორც ვებაპლიკაცია

## დამატებითი ინსტრუქცია
იხილეთ დეტალური ინსტრუქცია: https://github.com/თქვენი_რეპო 