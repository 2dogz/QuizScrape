# QuizScrape

This program is written in Python3 and is intended to go to a URL of a Quiz, Take the Question Div, write it to an output file, and move on to the next question in the quiz, until there are no more questions to add to the new file.

This is for my personal preference of seeing all the questions at one time instead of seeing them one by one on canvas. 


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install BS4. (python3 using alias)

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade bs4
```

Find The cookies you need in chrome -> right click -> inspect -> application -> storage -> cookies

Find The cookies you need in firefox -> right click -> inspect element -> storage -> cookies

```bash
python main.py
#Please enter your logSession Cookie data
LB9ZnMRIQPW9zAjG3q4ojHEWe4NUBvW5
#Please enter your legacySession Cookie data
Z966A61rrWjSI.kwM62VVM7oreZqz6u_BBckULWaJfHfOR1uvBe3sGmCjM4eY47VZLPt1bNKAnaXPH-K7ujIXSqaFx_5.VvKkbkMlfnh9oYAUTPgSDXm4cT0Ng0mShcoGvk6VgLx7VByOPhoBEGDUS4tvLxRQ_7viYTI-fswudmmis0A5HrzcSG9tfuVfSoCUset9MQgL-XFTVK94qqpK0cbGjU_7fs_UPe4NTKsk5od8h4sgITevqIQqLdtX0gBw_EESNo2jCue_AxTZz9sCB.QxgYrfirAw.N1O.n5SN4SFlZZsffpnyq.6w92J6fG7jimVzgTkjj4F9aThp.8RFL8dHVCRNH55XbgHudMeSHxVs4kWMZwvwT.L43Q3BLY2vTACgUrDMibAQmK6u1Z_Jvzym_Kmlu.aAwOm1P_wsG9KKFaQanCh3wod_8JwFGn23kn0KtBPon0tJDEXXgQZSbu3SL-OKmZbwN8VR63wqgwBZcupHymc8leP4Wz1SpU-eOcI65cGd_.KF.QnyDHysquCh9aq98m5noj0hxJWc1cK4LG3ZY4JibWsOcYJE9R-Tck6UCwhvlGWUjcP71HF53aTB1ClGtr2xwMLB3N5CDWqrgjLa8m1EjAe4f9s3QB0J.Z_bb2VrYny33l
#Please enter your canvasSession Cookie data
LxIb4jUHPe9cJSC8jHACJg+4MBvbuY41r_ABV6E-fTm9wQnKxgaKS4v3Uz2ZYxGs5aViin5Ubr9DzF8JSRWBsoIwpNMfhGX8ZktNteybsvRL8ZhPX8ORBWLnuB-SzeHvFhQKJ8IrkzwqygTv2yG4s0DXp_uiJZPT96VlWiBx8bI5yAkCeTdu8zXfIwK8Q7KnTwoVBI3jUkEc94zv50XBOprYHnCUitAZ_exGT5hMvbXwrR8sRe1L3t2jb6fgI4OxpEdMwFAG6TfhW8hW38rtOwRp-1Ujl_GbpZU9bTj0X1zNymvnV1iUEkGQhULjU58mru5O66VHSY4RwydLQYPprxQyTW2YlZMsahbq46gkrl6elq-YnUdKx4INkJaMjK-fN9LCqbbVTlUXZah0gofDsMfN-Kh2Xpn_Hzy8NWgJB9UfhBf1tg5yE8PR7c5qw8ubhdMv8WNj56Ybq_3mIcNSIyDbGlx9nW0JP8FLxTmWcaqMJu5iXEBUwkujV0Qj6ySJrvQ4kVcffBAX09t2xkrf0s5ZHxnMjH5bsddpQRZwkRgh2_QjFjP0GtU5W1eOxCmNj7xkpzoEvN7k6yjzv0R3Ng4XG6kp_wFaNTY689W2O03Og.PW7FvvI_-GwcozKVVwZGc-bMV2E.YEPtqw
#Please enter your csrf Cookie data
erwTEKUEBf8AK1jbVQL0PWy%7Q31OvRZVeWbhu2zL5llQynwe9xaUh3GZTraIp8IBFlE2u3TmATsdjQhvN5PWiNIqm%7atrMBD1M
#Please enter the url of the quiz
https://missouri.instructure.com/courses/11111/quizzes/111111/take/questions/1111111
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)