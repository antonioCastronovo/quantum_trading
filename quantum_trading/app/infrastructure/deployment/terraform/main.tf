resource "kubernetes_deployment" "quantum" {
  metadata {
    name = "quantum-trading"
  }
  spec {
    replicas = 3
    template {
      container {
        name  = "app"
        image = "quantum-trading:latest"
      }
    }
  }
}