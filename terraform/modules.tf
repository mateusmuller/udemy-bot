module "storage" {
  source = "./modules/storage"

  project-name = var.project-name
}

module "container" {
  source = "./modules/container"

  project-name = var.project-name
}

module "code" {
  source = "./modules/code"

  project-name = var.project-name
  s3_arn = module.storage.s3_arn
  ecr_url = module.container.ecr_url
}