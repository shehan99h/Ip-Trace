a
    1U�`�  �                   @   s  d dl mZ d dlZd dlZd dlZd dlZd dlZd dlm	Z	 d dl
mZ d dlmZ d dlmZ d dlmZmZ e�d� d	Zd
Zeed� G dd� d�Zedk�re� Zeed��Zedkr�ed�Zed�Ze�ee� n"edkr�ed�Z e�!e � ne"�  dS )�    )�print_functionN)�	MimeTypes)�build)�InstalledAppFlow)�Request)�MediaIoBaseDownload�MediaFileUpload�clearz=[1;33;40m
_________________________________________________
z�[1;32;40m
___________________________________________________________
[1;36;40m    [1] download file

[1;35;40m      [+] Tool By Shehan Lahiru
[1;32;40m___________________________________________________________
� c                   @   s*   e Zd Zdgadd� Zdd� Zdd� ZdS )	�DriveAPIz%https://www.googleapis.com/auth/drivec                 C   s  d | _ tj�d�rHtdd��}t�|�| _ W d   � n1 s>0    Y  | j rV| j js�| j r|| j jr|| j j	r|| j �
t� � nt�dt�}|jdd�| _ tdd��}t�| j |� W d   � n1 s�0    Y  tdd| j d	�| _| j�� jd
dd��� }|�dg �}d S )Nztoken.pickle�rbzcredentials.jsonr   )Zport�wbZdriveZv3)Zcredentials�d   zfiles(id, name))ZpageSize�fields�files)Zcreds�os�path�exists�open�pickle�loadZvalidZexpiredZrefresh_tokenZrefreshr   r   Zfrom_client_secrets_file�SCOPESZrun_local_server�dumpr   �servicer   �list�execute�get)�self�tokenZflowZresults�items� r    �?/data/data/com.termux/files/home/Ip-Trace/__init__/downloder.py�__init__2   s$    *�,
�
zDriveAPI.__init__c           	      C   s�   | j �� j|d�}t�� }t||dd�}d}z`|s@|�� \}}q.|�d� t|d��}t	�
||� W d   � n1 sv0    Y  td� W dS    td	� Y dS 0 d S )
N)ZfileIdi   )Z	chunksizeFr   r   zFile DownloadedTzSomething went wrong.)r   r   Z	get_media�io�BytesIOr   Z
next_chunk�seekr   �shutilZcopyfileobj�print)	r   Zfile_id�	file_nameZrequestZfhZ
downloaderZdoneZstatus�fr    r    r!   �FileDownload�   s    
*zDriveAPI.FileDownloadc                 C   sr   |� d�d }t� �|�d }d|i}z2t||d�}| j�� j||dd��� }td� W n   t	d	��Y n0 d S )
N�/�����r   �name)�mimetype�id)�bodyZ
media_bodyr   zFile Uploaded.zCan't Upload File.)
�splitr   Z
guess_typer   r   r   Zcreater   r'   ZUploadError)r   �filepathr-   r.   Zfile_metadataZmedia�filer    r    r!   �
FileUpload�   s    
�
zDriveAPI.FileUploadN)�__name__�
__module__�__qualname__r   r"   r*   r4   r    r    r    r!   r   &   s   g8r   �__main__zPress 1 and enter:�   zEnter file id: zEnter file name: �   zEnter full file path: )#Z
__future__r   r   �os.pathr   r#   r&   ZrequestsZ	mimetypesr   Zgoogleapiclient.discoveryr   Zgoogle_auth_oauthlib.flowr   Zgoogle.auth.transport.requestsr   Zgoogleapiclient.httpr   r   �systemZbarr-   r'   r   r5   �obj�int�input�iZf_idZf_namer*   Zf_pathr4   �exitr    r    r    r!   �<module>   s6   

 ]
