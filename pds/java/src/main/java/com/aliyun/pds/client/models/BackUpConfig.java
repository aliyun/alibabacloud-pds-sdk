// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class BackUpConfig extends TeaModel {
    // folder_id
    @NameInMap("folder_id")
    public String folderId;

    // photo_folder_id
    @NameInMap("photo_folder_id")
    public String photoFolderId;

    // sub_folder
    @NameInMap("sub_folder")
    public java.util.Map<String, ?> subFolder;

    // video_folder_id
    @NameInMap("video_folder_id")
    public String videoFolderId;

    public static BackUpConfig build(java.util.Map<String, ?> map) throws Exception {
        BackUpConfig self = new BackUpConfig();
        return TeaModel.build(map, self);
    }

    public BackUpConfig setFolderId(String folderId) {
        this.folderId = folderId;
        return this;
    }
    public String getFolderId() {
        return this.folderId;
    }

    public BackUpConfig setPhotoFolderId(String photoFolderId) {
        this.photoFolderId = photoFolderId;
        return this;
    }
    public String getPhotoFolderId() {
        return this.photoFolderId;
    }

    public BackUpConfig setSubFolder(java.util.Map<String, ?> subFolder) {
        this.subFolder = subFolder;
        return this;
    }
    public java.util.Map<String, ?> getSubFolder() {
        return this.subFolder;
    }

    public BackUpConfig setVideoFolderId(String videoFolderId) {
        this.videoFolderId = videoFolderId;
        return this;
    }
    public String getVideoFolderId() {
        return this.videoFolderId;
    }

}
