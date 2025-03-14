# Log Kits

Log Kits is a Python-based project designed for translating log protocols. It can receive logs in one format, such as syslog, and output them in another format, such as a webhook.

## Features

- Receive logs via syslog/webhook
- Output logs via syslog/webhook
- Easy to configure and extend

## Requirements

- Docker
- Docker Compose

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/wowtalon/log-kits.git
    cd log-kits
    ```

2. Build and run the project using Docker Compose:
    ```sh
    docker-compose up -d
    ```

## Usage

1. Configure the input and output settings in the `config.yaml` file.
2. Start the service using Docker Compose:
    ```sh
    docker-compose up
    ```

## Configuration

The `config.yaml` file allows you to specify the input and output settings. Here is an example configuration:

```yaml
workflows:
  - name: "workflow2"
    enabled: false
    steps:
      - name: "step3"
        worker: "syslog"
        command: "echo 'Goodbye, world!'"
        target: "localhost:5514"
      - name: "step3"
        worker: "base64"
        command: "encode"
        target: "localhost:5514"
      - name: "step1"
        worker: "webhook"
        command: "echo 'Hello, world!'"
        target:
          url: "http://localhost:8080"
          key: "ENV_VAR"
  - name: "workflow2"
    enabled: true
    steps:
      - name: "step1"
        worker: "webhook"
        command: "echo 'Hello, world!'"
        target:
          url: "http://localhost:8080"
          key: "ENV_VAR"
      - name: "step2"
        worker: "json"
        command: "data.msg"
        target: "localhost:5514"
      - name: "step3"
        worker: "base64"
        command: "encode"
        target: "localhost:5514"
      - name: "step3"
        worker: "syslog"
        command: "echo 'Goodbye, world!'"
        target: "localhost:5514"
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.