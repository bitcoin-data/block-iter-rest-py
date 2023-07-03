{ pkgs ? import <nixpkgs> {}, unstable-pkgs ? import <nixos-unstable/nixpkgs> {}}:
pkgs.mkShell {

    nativeBuildInputs = [
      pkgs.python3
      pkgs.python3Packages.flake8
      pkgs.python3Packages.autopep8
      pkgs.python3Packages.requests
    ];

}
