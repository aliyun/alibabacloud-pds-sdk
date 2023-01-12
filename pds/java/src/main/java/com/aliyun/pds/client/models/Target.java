// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class Target extends TeaModel {
    /**
     * <p>FileID</p>
     */
    @NameInMap("file_id")
    public String fileId;

    /**
     * <p>FileName</p>
     */
    @NameInMap("file_name")
    public String fileName;

    /**
     * <p>FileType</p>
     */
    @NameInMap("file_type")
    public String fileType;

    public static Target build(java.util.Map<String, ?> map) throws Exception {
        Target self = new Target();
        return TeaModel.build(map, self);
    }

    public Target setFileId(String fileId) {
        this.fileId = fileId;
        return this;
    }
    public String getFileId() {
        return this.fileId;
    }

    public Target setFileName(String fileName) {
        this.fileName = fileName;
        return this;
    }
    public String getFileName() {
        return this.fileName;
    }

    public Target setFileType(String fileType) {
        this.fileType = fileType;
        return this;
    }
    public String getFileType() {
        return this.fileType;
    }

}
