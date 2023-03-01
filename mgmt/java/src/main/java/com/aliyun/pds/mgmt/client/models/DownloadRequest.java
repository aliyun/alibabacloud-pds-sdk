// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 下载文件请求body
 */
public class DownloadRequest extends TeaModel {
    /**
     * <p>drive id</p>
     */
    @NameInMap("DriveID")
    public String DriveID;

    /**
     * <p>file id</p>
     */
    @NameInMap("FileID")
    @Validation(required = true)
    public String FileID;

    /**
     * <p>in: query</p>
     * <p>image_thumbnail_process</p>
     */
    @NameInMap("ImageThumbnailProcess")
    public String ImageThumbnailProcess;

    /**
     * <p>office_thumbnail_process</p>
     */
    @NameInMap("OfficeThumbnailProcess")
    public String OfficeThumbnailProcess;

    /**
     * <p>revision id</p>
     */
    @NameInMap("RevisionID")
    public String RevisionID;

    /**
     * <p>share_id, either share_id or drive_id is required</p>
     */
    @NameInMap("ShareID")
    public String ShareID;

    /**
     * <p>video_thumbnail_process</p>
     * <p>type:string</p>
     */
    @NameInMap("VideoThumbnailProcess")
    public String VideoThumbnailProcess;

    /**
     * <p>addition_data</p>
     */
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    @NameInMap("file_id_path")
    public String fileIdPath;

    /**
     * <p>location</p>
     */
    @NameInMap("location")
    public String location;

    @NameInMap("referer")
    public String referer;

    @NameInMap("sign_token")
    public String signToken;

    public static DownloadRequest build(java.util.Map<String, ?> map) throws Exception {
        DownloadRequest self = new DownloadRequest();
        return TeaModel.build(map, self);
    }

    public DownloadRequest setDriveID(String DriveID) {
        this.DriveID = DriveID;
        return this;
    }
    public String getDriveID() {
        return this.DriveID;
    }

    public DownloadRequest setFileID(String FileID) {
        this.FileID = FileID;
        return this;
    }
    public String getFileID() {
        return this.FileID;
    }

    public DownloadRequest setImageThumbnailProcess(String ImageThumbnailProcess) {
        this.ImageThumbnailProcess = ImageThumbnailProcess;
        return this;
    }
    public String getImageThumbnailProcess() {
        return this.ImageThumbnailProcess;
    }

    public DownloadRequest setOfficeThumbnailProcess(String OfficeThumbnailProcess) {
        this.OfficeThumbnailProcess = OfficeThumbnailProcess;
        return this;
    }
    public String getOfficeThumbnailProcess() {
        return this.OfficeThumbnailProcess;
    }

    public DownloadRequest setRevisionID(String RevisionID) {
        this.RevisionID = RevisionID;
        return this;
    }
    public String getRevisionID() {
        return this.RevisionID;
    }

    public DownloadRequest setShareID(String ShareID) {
        this.ShareID = ShareID;
        return this;
    }
    public String getShareID() {
        return this.ShareID;
    }

    public DownloadRequest setVideoThumbnailProcess(String VideoThumbnailProcess) {
        this.VideoThumbnailProcess = VideoThumbnailProcess;
        return this;
    }
    public String getVideoThumbnailProcess() {
        return this.VideoThumbnailProcess;
    }

    public DownloadRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public DownloadRequest setFileIdPath(String fileIdPath) {
        this.fileIdPath = fileIdPath;
        return this;
    }
    public String getFileIdPath() {
        return this.fileIdPath;
    }

    public DownloadRequest setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public DownloadRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public DownloadRequest setSignToken(String signToken) {
        this.signToken = signToken;
        return this;
    }
    public String getSignToken() {
        return this.signToken;
    }

}
