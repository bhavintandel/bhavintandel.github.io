# AWS GluePyspark Locally

## Download and install maven

1. Download maven from <https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-common/apache-maven-3.6.0-bin.tar.gz>
2. untar the content to respective folder
   For example, `mv apache-maven-3.6.0 {HOME}/Documents/opt/apache-maven`
3. Add mvn to your path

    ```bash
    echo 'export PATH=$PATH:/Users/bhavintandel/Documents/opt/apache-maven/bin' >> ~/.profile
    ```

4. Restart the session

## Download the Spark distrubution

At the moment aws provide two glue spark executable,

* Glue version 0.9: <https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-0.9/spark-2.2.1-bin-hadoop2.7.tgz>
* Glue version 1.0: <https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-1.0/spark-2.4.3-bin-hadoop2.8.tgz>

 1. Download the spark executables and move it to respective folder.
 2. Export the SPARK_HOME,
 `export SPARK_HOME=$HOME/Documents/opt/spark/latest`
  You can also add it to your ~/.profile file.

## Download the aws-glue-libs

Aws have two version for aws-glue-libs,

* 0.9 -> python2 -> git@github.com:awslabs/aws-glue-libs.git 
* 1.0 -> support python3 -> git@github.com:awslabs/aws-glue-libs.git

1. Clone the aws-glue-libs repo,
  For specific branch, 
  `git clone -b {branch-name} git@github.com:awslabs/aws-glue-libs.git`
2. Run the gluepyspark

    ```bash
    cd aws-glue-libs
    ./bin/gluepyspark
    ```

## Configure pycharm for pyspark development

1. Install pyspark as python package
