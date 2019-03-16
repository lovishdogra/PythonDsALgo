workflow "Python Lister" {
  on = "push"
  resolves = ["The Python Action"]
}

action "The Python Action" {
  uses = "Gr1N/the-python-action@0.4.0"
}
