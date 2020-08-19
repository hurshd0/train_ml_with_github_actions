## Demo showcasing simple MLOps workflow

### Follow below instructions to try out 👇

1. Fork this repo 🍴

![](https://i.imgur.com/3fjO1eA.png)

2. Checkout a branch and test out a different ML model via `git checkout -b random_forest` 

3. Add ML classifier of your choice to `titanic_model/pipeline.py`
![](https://i.imgur.com/jiDyhmW.png)

4. Sign In to AWS Account and create S3 bucket (in N. Virginia) and some folders  
Follow this guide if you don't know: [How do I create an S3 Bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)
**Should look exactly like**👇
![](https://i.imgur.com/GX3cV1B.png)

5. Go to IAM Console and create AWS Access Keys, store them in safe place

[How do I set up an IAM user and sign in to the AWS Management Console using IAM credentials?](https://www.youtube.com/watch?v=wRzzBb18qUw)
[How do I create an access key for an existing IAM user?](https://www.youtube.com/watch?v=JvtmmS9_tfU)

Some tips:
- For beginners create Admin user with full access
- For advanced users create a user with only access to that bucket, follow this, [How To Grant Access To Only One S3 Bucket Using AWS IAM Policy](https://objectivefs.com/howto/how-to-restrict-s3-bucket-policy-to-only-one-aws-s3-bucket)

6. Add your AWS `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to Github Secrets
![](https://i.imgur.com/LdWJk4V.png)

7 Create a Pull Request to master
![](https://i.imgur.com/yhUaqXu.png)

8 Go get a sip of ☕ while your model trains
Once traininig is completed it should look like this
![](https://i.imgur.com/4NWGQXp.gif)

### To run it locally follow below instructions

#### Pre-requisites

- Python 3
- Conda [Optional, but recommended]

1. If you have conda, than install `pipenv` via `conda install pipenv`, if you don't just do `pip install pipenv`
2. To install dependencies do `pipenv install`
3. To activate virtual environment do `pipenv shell`
4. Run Jupyter Notebook by `jupyter notebook` command
5. Run `tox` to train ML model and generate reports, and pickled model saved in `titanic_model/trained_model_artifacts`

#### Project structure
```
.
├── notebooks
└── titanic_model
    ├── config
    ├── processing
    └── trained_model_artifacts

5 directories
```
