// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.standard.client.models;

import com.aliyun.tea.*;

/**
 * play_media request
 */
public class PlayMediaRequest extends TeaModel {
    // auth_key
    @NameInMap("AuthKey")
    @Validation(required = true, pattern = "[a-z0-9]+")
    public String AuthKey;

    // drive_id
    @NameInMap("DriveID")
    @Validation(required = true, pattern = "[0-9]+")
    public String DriveID;

    // file_id
    @NameInMap("FileID")
    @Validation(required = true, pattern = "[a-z0-9.-_]{1,50}", maxLength = 50, minLength = 40)
    public String FileID;

    public static PlayMediaRequest build(java.util.Map<String, ?> map) throws Exception {
        PlayMediaRequest self = new PlayMediaRequest();
        return TeaModel.build(map, self);
    }

    public PlayMediaRequest setAuthKey(String AuthKey) {
        this.AuthKey = AuthKey;
        return this;
    }
    public String getAuthKey() {
        return this.AuthKey;
    }

    public PlayMediaRequest setDriveID(String DriveID) {
        this.DriveID = DriveID;
        return this;
    }
    public String getDriveID() {
        return this.DriveID;
    }

    public PlayMediaRequest setFileID(String FileID) {
        this.FileID = FileID;
        return this;
    }
    public String getFileID() {
        return this.FileID;
    }

}
