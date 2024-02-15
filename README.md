
# Running tensorflow in a vagrant box installation

In this repo we will check out how to create our own easy to run vagrant box with a preset of:

- Tensorflow 2.15.0
- Python 3.10.12
- pip 22.0.2
- Ubuntu 22.04 (bento/ubuntu-22.04)

NOTE: The official box could be found at: https://app.vagrantup.com/JeffersonPino/boxes/ubuntu-tensorflow



## Download and installing our box

After checking out the main branch three files will be downloaded:

- check-tensorflow-version.py
- tensorflow-mnist-example.py
- Vagrantfile

The Vagranfile cointains all the code needed to install our new ubuntu node.

Once we are located inside our project folder, run:

This will start up our vagran enviroment:
```bash
  vagrant init 
```

We can now start downloading and initilizing our machine:
```bash
  vagrant up 
```

## Connecting to our box.

we can check if our box was succesfully installed with the following command:

This command is going to list all available vagrant boxes running:
```bash
  vagrant status 
```

In order to connect to our box, we need to run the following command:

If everything went as planned we must see our ubuntu command line:
```bash
  vagrant ssh tensorFlowClient 
```

## Executing our tensorflow test.

Our Vagrantfile already includes a line for setting up a shared folder between our machine and host. This will allow us to transfer easly files between machine.

```bash
  tensorFlowClient.vm.synced_folder "./sharedFolder", "/home/vagrant/sharedFolder" 
```

First, let's navigate to this folder inside our server:

```bash
  cd /home/vagrant/sharedFolder
```
Inside this folder there will be two files:
- check-tensorflow-version.py
- tensorflow-mnist-example.py

Both files could be executed by running:
```bash
  python3 check-tensorflow-version.py
```
This will print out the current version of our tensorflow installation.

Our second test will use more complex libraries such as Keras, which will allow us to run a keras default model included in our tensorflow installation called mnist. (https://www.tensorflow.org/datasets/catalog/mnist?hl=es-419) 
```bash
  python3 tensorflow-mnist-example.py
```
If everything runs as planned, we will see our prediction result printing in the terminal.
