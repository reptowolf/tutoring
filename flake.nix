{
  inputs = { nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable"; };
  outputs = { self, nixpkgs }:
    let pkgs = nixpkgs.legacyPackages.x86_64-linux.pkgs;
    in {
      devShells.x86_64-linux.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          nil
          nixfmt
          python310
          python310Packages.python-lsp-server
          python310Packages.autopep8
          python310Packages.evdev
          # python310Packages.pylint
          # python310Packages.flake8
        ];
      };
    };
}
