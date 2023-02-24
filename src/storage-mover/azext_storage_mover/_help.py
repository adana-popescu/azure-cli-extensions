# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from knack.help_files import helps  # pylint: disable=unused-import

helps['storage-mover endpoint create-for-storage-container'] = """
type: command
short-summary: Creates an Endpoint resource for storage blob container.
examples:
    - name: endpoint create-for-storage-container
      text: >
        az storage-mover endpoint create-for-storage-container -g {rg} --storage-mover-name {mover_name} -n
        {endpoint_container} --container-name {container_name} --storage-account-id {account_id} --description endpointDesc
"""

helps['storage-mover endpoint create-for-nfs'] = """
type: command
short-summary: Creates an Endpoint resource for nfs.
examples:
    - name: endpoint create-for-nfs
      text: >
        az storage-mover endpoint create-for-nfs -g {rg} --storage-mover-name {mover_name} -n {endpoint_nfs}
        --description endpointDesc --export exportfolder --nfs-version NFSv4 --host {vm_ip}
"""

helps['storage-mover endpoint update-for-storage-container'] = """
type: command
short-summary: Updates an Endpoint resource for storage blob container.
examples:
    - name: endpoint update-for-storage-container
      text: >
        az storage-mover endpoint update-for-storage-container -g {rg} --storage-mover-name {mover_name} -n
        {endpoint_container} --description endpointDescUpdate --container-name {container_name} --storage-account-id {account_id}
"""

helps['storage-mover endpoint update-for-nfs'] = """
type: command
short-summary: Updates an Endpoint resource for nfs.
examples:
    - name: endpoint update-for-nfs
      text: >
        az storage-mover endpoint update-for-nfs -g {rg} --storage-mover-name {mover_name} -n {endpoint_nfs}
        --description endpointDescUpdate --export exportfolder --nfs-version NFSv4 --host {vm_ip}
"""