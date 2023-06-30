# RabbitMQ test

All code in this repository is either copied from or based on [simulation-tools](https://github.com/simcesplatform/simulation-tools) repository.

To start the test (only the file `docker-compose.yml` needed):

```bash
docker compose up --abort-on-container-exit
```

To remove the test containers and networks:

```bash
docker compose down
```

Excerpt from the end of the output of a successful test:

```text
...
...
test_test      | 2023-06-30T09:41:13.625 ---     INFO --- Sending a simulation state message stopped
test_test      | 2023-06-30T09:41:13.626 ---     INFO ---
test_test      | 2023-06-30T09:41:13.633 ---    DEBUG --- Message '{"Type": "SimState", "SimulationId": "2000-01-01T12:00:00.000Z", "Timestamp": "2023-06-30T09:41:13.625Z", "SourceProcessId": "TestProcess", "MessageId": "TestProcess-5", "SimulationState": "stopped"}' send to topic: 'SimState'
test_test      | 2023-06-30T09:41:13.633 ---    DEBUG --- Message '{"Type": "SimState", "SimulationId": "2000-01-01T12:00:00.000Z", "Timestamp": "2023-06-30T09:41:13.625Z", "SourceProcessId": "TestProcess", "MessageId": "TestProcess-5", "SimulationState": "stopped"}' received from topic: 'SimState'
test_test      | 2023-06-30T09:41:13.634 ---     INFO --- Received simulation state message 'stopped' from 'TestProcess'
test_test      | 2023-06-30T09:41:13.635 ---     INFO ---
test_test      | 2023-06-30T09:41:13.635 ---     INFO --- Received 'SimState' message from topic 'SimState'
test_test      | 2023-06-30T09:41:13.635 ---     INFO --- Full message: {"Type": "SimState", "SimulationId": "2000-01-01T12:00:00.000Z", "Timestamp": "2023-06-30T09:41:13.625Z", "SourceProcessId": "TestProcess", "MessageId": "TestProcess-5", "SimulationState": "stopped"}
test_test      | 2023-06-30T09:41:13.635 ---     INFO ---
test_test      | 2023-06-30T09:41:13.636 ---     INFO --- Total of 5 messages received
test_test      | 2023-06-30T09:41:13.636 ---     INFO --- Latest epoch number recorded is: 3
test_test      | 2023-06-30T09:41:15.567 ---     INFO --- Receiver: Closing the connection to the message bus.
test_test      | Robust channel <RobustChannel "None#Not initialized channel"> has been closed.
test_test      | NoneType: None
test_rabbitmq  | 2023-06-30 09:41:15.590 [info] <0.914.0> closing AMQP connection <0.914.0> (172.30.0.1:46374 -> 172.30.0.2:5672, vhost: '/', user: 'guest')
test_rabbitmq  | 2023-06-30 09:41:15.591 [info] <0.1009.0> Closing all channels from connection '172.30.0.1:46374 -> 172.30.0.2:5672' because it has been closed
test_test      | 2023-06-30T09:41:17.630 ---     INFO --- Sender: Closing the connection to the message bus.
test_rabbitmq  | 2023-06-30 09:41:17.640 [info] <0.941.0> closing AMQP connection <0.941.0> (172.30.0.1:57304 -> 172.30.0.2:5672, vhost: '/', user: 'guest')
test_rabbitmq  | 2023-06-30 09:41:17.645 [info] <0.1020.0> Closing all channels from connection '172.30.0.1:57304 -> 172.30.0.2:5672' because it has been closed
test_test      | 2023-06-30T09:41:17.645 ---     INFO --- Closing the test process
test_test exited with code 0
Aborting on container exit...
[+] Running 2/2
 ✔ Container test_test      Stopped                                                                                0.0s
 ✔ Container test_rabbitmq  Stopped                                                                                1.5s
```
