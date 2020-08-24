<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 下载文件请求body.
 */
class DownloadRequest extends Model
{
    /**
     * @description drive id
     *
     * @example 1
     *
     * @var string
     */
    public $DriveID;

    /**
     * @description file id
     *
     * @example 5d79206586bb5dd69fb34c349282718146c55da7
     *
     * @var string
     */
    public $FileID;

    /**
     * @description in: query
     * image_thumbnail_process
     * @example image/resize,m_fill,h_128,w_128,limit_0
     *
     * @var string
     */
    public $ImageThumbnailProcess;

    /**
     * @description share_id, either share_id or drive_id is required
     *
     * @example 0018d25b-faed-4f5c-a67b-414e160b7953
     *
     * @var string
     */
    public $ShareID;

    /**
     * @description video_thumbnail_process
     * type:string
     * @example video/snapshot,t_7000,f_jpg,w_800,h_600,m_fast
     *
     * @var string
     */
    public $VideoThumbnailProcess;
    protected $_name = [
        'DriveID'               => 'DriveID',
        'FileID'                => 'FileID',
        'ImageThumbnailProcess' => 'ImageThumbnailProcess',
        'ShareID'               => 'ShareID',
        'VideoThumbnailProcess' => 'VideoThumbnailProcess',
    ];

    public function validate()
    {
        Model::validateRequired('FileID', $this->FileID, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->DriveID) {
            $res['DriveID'] = $this->DriveID;
        }
        if (null !== $this->FileID) {
            $res['FileID'] = $this->FileID;
        }
        if (null !== $this->ImageThumbnailProcess) {
            $res['ImageThumbnailProcess'] = $this->ImageThumbnailProcess;
        }
        if (null !== $this->ShareID) {
            $res['ShareID'] = $this->ShareID;
        }
        if (null !== $this->VideoThumbnailProcess) {
            $res['VideoThumbnailProcess'] = $this->VideoThumbnailProcess;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return DownloadRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['DriveID'])) {
            $model->DriveID = $map['DriveID'];
        }
        if (isset($map['FileID'])) {
            $model->FileID = $map['FileID'];
        }
        if (isset($map['ImageThumbnailProcess'])) {
            $model->ImageThumbnailProcess = $map['ImageThumbnailProcess'];
        }
        if (isset($map['ShareID'])) {
            $model->ShareID = $map['ShareID'];
        }
        if (isset($map['VideoThumbnailProcess'])) {
            $model->VideoThumbnailProcess = $map['VideoThumbnailProcess'];
        }

        return $model;
    }
}
