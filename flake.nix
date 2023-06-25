{
  inputs = { nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable"; };
  outputs = { self, nixpkgs }:
    let pkgs = nixpkgs.legacyPackages.x86_64-linux.pkgs;
    in {
      devShells.x86_64-linux.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          nil
          nixfmt
          python311
          python311Packages.python-lsp-server
          python311Packages.autopep8
          python311Packages.evdev
          # python311Packages.pylint
          # python311Packages.flake8
        ];
      };
    };
}
