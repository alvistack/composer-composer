# Composer initialization script

export COMPOSER_ALLOW_SUPERUSER="1"

# Add path to commands installed using "composer global require ..."
if [ "${EUID:-0}" != "0" ]; then
  case :$PATH: in
    *:${HOME}/.composer/vendor/bin:*) ;;
    *) PATH=$PATH:${HOME}/.composer/vendor/bin ;;
  esac
  export PATH
fi
