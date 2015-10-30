# Rename 'hammerhead' and other values as appropriate
cat <<'EOF' >droid-hal-hammerhead.spec
# These and other macros are documented in dhd/droid-hal-device.inc
%define device cancro
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Mi 3
%define installable_zip 1
%include rpm/dhd/droid-hal-device.inc

