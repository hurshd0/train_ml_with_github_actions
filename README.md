## Demo showcasing simple MLOps workflow

### Follow below instructions to try out 👇

1. Fork this repo 🍴

![](https://i.imgur.com/3fjO1eA.png)

2. Sign In to AWS Account and create S3 bucket (in N. Virginia) and some folders  

Follow this guide if you don't know: [How do I create an S3 Bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)

**Should look exactly like**👇

![](https://i.imgur.com/GX3cV1B.png)

3. Go to IAM Console and create AWS Access Keys, store them in safe place

[How do I set up an IAM user and sign in to the AWS Management Console using IAM credentials?](https://www.youtube.com/watch?v=wRzzBb18qUw)

[How do I create an access key for an existing IAM user?](https://www.youtube.com/watch?v=JvtmmS9_tfU)

Some tips:
- For beginners create Admin user with full access
- For advanced users create a user with only access to that bucket, follow this, [How To Grant Access To Only One S3 Bucket Using AWS IAM Policy](https://objectivefs.com/howto/how-to-restrict-s3-bucket-policy-to-only-one-aws-s3-bucket)

5. Install AWS CLI, I'm using WS on Windows, so I did `python -m pip install --user awscli` to install as global package

For more detail instructions follow, https://github.com/aws/aws-cli 

6. Configure AWS credentials
```
$ aws configure
AWS Access Key ID: MYACCESSKEY
AWS Secret Access Key: MYSECRETKEY
Default region name [us-west-2]: us-west-2
Default output format [None]: json
```
7. Download the raw dataset  

a. Dataset: https://titanic-model.s3.amazonaws.com/raw_titanic.csv
b. Create a folder inside `titanic_model` called `data`, 
following is project structure that should look like
```
.
├── notebooks
└── titanic_model
    ├── data
    ├── config
    ├── processing
    └── trained_model_artifacts

5 directories
```
8. Install packade dependencies and run it locally to verify if it works

#### Pre-requisites

- Python 3
- Conda [Optional, but recommended]

a. If you have conda, than install `pipenv` via `conda install pipenv`, if you don't just do `pip install pipenv`
b. To install dependencies do `pipenv install`
c. To activate virtual environment do `pipenv shell`
d. `cd` into `titanic_model` & do `dvc remote add data` which adds `data` folder so it can be tracked by __DVC__

NOTE: If you have any issues visit: https://dvc.org/doc/user-guide/external-dependencies

e. Run `tox` to train ML model and generate reports, and pickled model saved in `titanic_model/trained_model_artifacts`

9. Checkout a branch and test out a different ML model via `git checkout -b random_forest` 

10. Add ML classifier of your choice to `titanic_model/pipeline.py`
![](https://i.imgur.com/jiDyhmW.png)

11. Add your AWS `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to Github Secrets
![](https://i.imgur.com/LdWJk4V.png)

12. Create a Pull Request to master
![](https://i.imgur.com/yhUaqXu.png)

13. Go get a sip of ☕ while your model trains
Once traininig is completed it should look like this
![](https://i.imgur.com/4NWGQXp.gif)
