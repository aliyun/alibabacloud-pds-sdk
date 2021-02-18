<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * create_share_link request.
 */
class CreateShareLinkRequest extends Model
{
    public $headers;

    /**
     * @description description
     *
     * @example desc
     *
     * @var string
     */
    public $description;

    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @description expiration
     *
     * @example 2006-01-02T15:04:05.999Z
     *
     * @var string
     */
    public $expiration;

    /**
     * @description file_id
     *
     * @example 5d5b846942cf94fa72324c14a4bda34e81da635d
     *
     * @var string
     */
    public $fileId;

    /**
     * @description file_id_list
     *
     * @example 5d5b846942cf94fa72324c14a4bda34e81da635d
     *
     * @var string[]
     */
    public $fileIdList;

    /**
     * @description file_path_list
     *
     * @example /a/
     *
     * @var string[]
     */
    public $filePathList;

    /**
     * @description share_name
     *
     * @example name
     *
     * @var string
     */
    public $shareName;

    /**
     * @description share_pwd
     *
     * @example 12ABcd
     *
     * @var string
     */
    public $sharePwd;
    protected $_name = [
        'description'  => 'description',
        'driveId'      => 'drive_id',
        'expiration'   => 'expiration',
        'fileId'       => 'file_id',
        'fileIdList'   => 'file_id_list',
        'filePathList' => 'file_path_list',
        'shareName'    => 'share_name',
        'sharePwd'     => 'share_pwd',
    ];

    public function validate()
    {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('expiration', $this->expiration, true);
        Model::validateRequired('fileId', $this->fileId, true);
        Model::validateRequired('fileIdList', $this->fileIdList, true);
        Model::validateRequired('filePathList', $this->filePathList, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validateMaximum('fileIdList', $this->fileIdList, 50);
        Model::validateMaximum('filePathList', $this->filePathList, 50);
        Model::validateMaximum('sharePwd', $this->sharePwd, 64);
        Model::validateMinimum('fileIdList', $this->fileIdList, 1);
        Model::validateMinimum('filePathList', $this->filePathList, 1);
        Model::validateMinimum('sharePwd', $this->sharePwd, 0);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->description) {
            $res['description'] = $this->description;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->expiration) {
            $res['expiration'] = $this->expiration;
        }
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->fileIdList) {
            $res['file_id_list'] = $this->fileIdList;
        }
        if (null !== $this->filePathList) {
            $res['file_path_list'] = $this->filePathList;
        }
        if (null !== $this->shareName) {
            $res['share_name'] = $this->shareName;
        }
        if (null !== $this->sharePwd) {
            $res['share_pwd'] = $this->sharePwd;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CreateShareLinkRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['description'])) {
            $model->description = $map['description'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['expiration'])) {
            $model->expiration = $map['expiration'];
        }
        if (isset($map['file_id'])) {
            $model->fileId = $map['file_id'];
        }
        if (isset($map['file_id_list'])) {
            if (!empty($map['file_id_list'])) {
                $model->fileIdList = $map['file_id_list'];
            }
        }
        if (isset($map['file_path_list'])) {
            if (!empty($map['file_path_list'])) {
                $model->filePathList = $map['file_path_list'];
            }
        }
        if (isset($map['share_name'])) {
            $model->shareName = $map['share_name'];
        }
        if (isset($map['share_pwd'])) {
            $model->sharePwd = $map['share_pwd'];
        }

        return $model;
    }
}
