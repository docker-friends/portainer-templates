

# Portainer Templates

Welcome to the community-driven **Portainer Templates** repository! 🚢

This project provides a community-maintained Portainer Template with a huge collection of Docker apps. This is designed to streamline and enhance your experience with [Portainer](https://www.portainer.io/), making it easier than ever to deploy and manage containerized applications.

## 📖 About

These templates provide pre-configured, ready-to-use setups for popular containerized applications, helping you quickly deploy services without the need to manually write complex configurations.

This repository is community-maintained, meaning anyone can contribute by adding, updating, or improving templates. Together, we can build a robust library of useful templates for the entire Portainer community!

**NOTE**: Each and every App in this template is tested and **FULLY WORKING** with the `latest` tag for the images.

## 👆 1-Click Deployment of Docker Apps

In the Portainer Dashboard, go to `Templates > Application`, select the desired Docker app from the list and click the `Deploy the container` button. 

That's it! Your Docker app will be ready to use after the processing is complete.

![portainer template deployment demo](https://raw.githubusercontent.com/docker-friends/portainer-templates/refs/heads/main/img/portainer-templates-deployment.gif)

## 🛠 Features

- **1-Click Deployment**: Deploy Docker containers with just 1 click.

- **Community-Powered**: Contributions from Docker enthusiasts around the globe.

- **Diverse Templates**: A wide range of applications in the templates, from databases to web servers and more.

- **Easy Integration**: Use directly with Portainer's App Templates feature.

- **Customizable**: Modify the templates to suit your specific needs.

## 🚀 Getting Started

### Using the Templates

1. In Portainer, navigate to **Settings > App Templates**.

![portainer settings](https://raw.githubusercontent.com/docker-friends/portainer-templates/refs/heads/main/img/portainer-templates-settings.png)

2. Add the following URL of the `app-templates.json` file from this repository in the App Template `URL` field:

	```bash
	https://raw.githubusercontent.com/docker-friends/portainer-templates/refs/heads/main/app-templates.json
 	```

4. Save the settings and explore the templates under `Templates > Application` section in Portainer.

### Contributing

We welcome contributions! Here's how you can help:

1. Fork this repository.

2. Create a branch for your template or improvement:

	```bash
	git checkout -b my-new-template
 	```

4. Add or modify a template in the `sources` directory.

5. Commit your changes and push to your branch:

	```bash
	git commit -m "Add new template for [application]"
	git push origin my-new-template
	```

6. Submit a pull request for review.

Please ensure your template follows the [Portainer Template Format](https://docs.portainer.io/advanced/app-templates/format).

### Issues & Feedback

If you encounter any issues or have suggestions for new templates, feel free to open an issue. Community feedback is invaluable in making this project better!

## 📚 Resources

[Portainer Documentation](https://docs.portainer.io/)

[Portainer Templates Guide](https://docs.portainer.io/advanced/app-templates)

## 📜 License

This repository is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. Feel free to use, modify, and distribute these templates as needed.

## 🙏 Acknowledgements

Inspired by and partial code reused from:

 - [@lissy93](https://github.com/Lissy93/portainer-templates)
 - [@shmolf](https://github.com/shmolf/portainer-templates)

## 🤝 Contributors

Thanks to all the amazing contributors who have made this project possible! 🙌
