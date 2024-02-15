
# Running tensorflow in a vagrant box installation

In this repo we will check out how to create our easy-to-run vagrant box with a preset of:

- Tensorflow 2.15.0
- Python 3.10.12
- pip 22.0.2
- Ubuntu 22.04

NOTE: The official box can be found at: https://app.vagrantup.com/JeffersonPino/boxes/ubuntu-tensorflow



## Download and installing our box

After checking out the main branch three files will be downloaded:

- check-tensorflow-version.py
- tensorflow-mnist-example.py
- Vagrantfile

The Vagranfile contains all the code needed to install our new Ubuntu node.

Once we are located inside our project folder, run the following:

This will start up our vagrant environment:
```bash
  vagrant init 
```

We can now start downloading and initializing our machine:
```bash
  vagrant up 
```

## Connecting to our box.

we can check if our box was successfully installed with the following command:

This command is going to list all available vagrant boxes running:
```bash
  vagrant status 
```

To connect to our box, we need to run the following command:

If everything went as planned we must see our Ubuntu command line:
```bash
  vagrant ssh tensorFlowClient 
```

## Executing our tensorflow test.

Our Vagrantfile already includes a line for setting up a shared folder between our machine and host. This will allow us to transfer easily files between machines.

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

Our second test will use more complex libraries such as Keras, allowing us to run a Keras default model included in our tensorflow installation called mnist. (https://www.tensorflow.org/datasets/catalog/mnist?hl=es-419) 
```bash
  python3 tensorflow-mnist-example.py
```
We will see our predicted result printing in the terminal if everything runs as planned.
