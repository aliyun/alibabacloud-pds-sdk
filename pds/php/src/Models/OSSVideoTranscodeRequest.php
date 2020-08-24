<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 启动视频转码请求
 */
class OSSVideoTranscodeRequest extends Model
{
    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @description file_path
     *
     * @example /a/b/c.mp4
     *
     * @var string
     */
    public $filePath;

    /**
     * @description hls_time
     *
     * @example 10
     *
     * @var int
     */
    public $hlsTime;

    /**
     * @description protection_scheme
     *
     * @example cbcs
     *
     * @var string
     */
    public $protectionScheme;

    /**
     * @description remarks
     *
     * @example {"userID":"xxx"}
     *
     * @var string
     */
    public $remarks;

    /**
     * @description share_id
     *
     * @example 3d336314-63c8-4d96-bce0-17aefb6833b6
     *
     * @var string
     */
    public $shareId;

    /**
     * @description transcode
     *
     * @example true
     *
     * @var bool
     */
    public $transcode;
    protected $_name = [
        'driveId'          => 'drive_id',
        'filePath'         => 'file_path',
        'hlsTime'          => 'hls_time',
        'protectionScheme' => 'protection_scheme',
        'remarks'          => 'remarks',
        'shareId'          => 'share_id',
        'transcode'        => 'transcode',
    ];
    protected $_default = [
        'protectionScheme' => 'none',
        'transcode'        => 'false',
    ];

    public function validate()
    {
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('shareId', $this->shareId, '[0-9a-zA-Z-]+');
        Model::validateRequired('filePath', $this->filePath, true);
        Model::validateMaxLength('filePath', $this->filePath, 1000);
        Model::validateMinLength('filePath', $this->filePath, 1);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->filePath) {
            $res['file_path'] = $this->filePath;
        }
        if (null !== $this->hlsTime) {
            $res['hls_time'] = $this->hlsTime;
        }
        if (null !== $this->protectionScheme) {
            $res['protection_scheme'] = $this->protectionScheme;
        }
        if (null !== $this->remarks) {
            $res['remarks'] = $this->remarks;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->transcode) {
            $res['transcode'] = $this->transcode;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return OSSVideoTranscodeRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['file_path'])) {
            $model->filePath = $map['file_path'];
        }
        if (isset($map['hls_time'])) {
            $model->hlsTime = $map['hls_time'];
        }
        if (isset($map['protection_scheme'])) {
            $model->protectionScheme = $map['protection_scheme'];
        }
        if (isset($map['remarks'])) {
            $model->remarks = $map['remarks'];
        }
        if (isset($map['share_id'])) {
            $model->shareId = $map['share_id'];
        }
        if (isset($map['transcode'])) {
            $model->transcode = $map['transcode'];
        }

        return $model;
    }
}
