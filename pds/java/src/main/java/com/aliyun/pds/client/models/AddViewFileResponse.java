// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * add file to view response
 */
public class AddViewFileResponse extends TeaModel {
    @NameInMap("drive_id")
    public String driveId;

    @NameInMap("file_id")
    public String fileId;

    @NameInMap("view_id")
    public String viewId;

    public static AddViewFileResponse build(java.util.Map<String, ?> map) throws Exception {
        AddViewFileResponse self = new AddViewFileResponse();
        return TeaModel.build(map, self);
    }

    public AddViewFileResponse setDriveId(String driveId) {
        this.driveId = driveId;
        return this;
    }
    public String getDriveId() {
        return this.driveId;
    }

    public AddViewFileResponse setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public AddViewFileResponse setViewId(String viewId) {
        this.viewId = viewId;
        return this;
    }
    public String getViewId() {
        return this.viewId;
    }

}
