<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\Hosting\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取文件下载地址的请求body
 */
class GetDownloadUrlRequest extends Model {
    protected $_name = [
        'additionData' => 'addition_data',
        'driveId' => 'drive_id',
        'expireSec' => 'expire_sec',
        'fileId' => 'file_id',
        'fileIdPath' => 'file_id_path',
        'fileName' => 'file_name',
        'location' => 'location',
        'referer' => 'referer',
        'shareId' => 'share_id',
        'signToken' => 'sign_token',
    ];
    protected $_default = [
        'expireSec' => 900,
    ];
    public function validate() {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('fileId', $this->fileId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('fileId', $this->fileId, '[a-z0-9.-_]{1,50}');
        Model::validateMaximum('expireSec', $this->expireSec, 14400);
        Model::validateMinimum('expireSec', $this->expireSec, 1);
        Model::validateMaxLength('fileId', $this->fileId, 50);
        Model::validateMaxLength('fileName', $this->fileName, 1024);
        Model::validateMinLength('fileId', $this->fileId, 40);
        Model::validateMinLength('fileName', $this->fileName, 1);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->expireSec) {
            $res['expire_sec'] = $this->expireSec;
        }
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->fileIdPath) {
            $res['file_id_path'] = $this->fileIdPath;
        }
        if (null !== $this->fileName) {
            $res['file_name'] = $this->fileName;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
        if (null !== $this->referer) {
            $res['referer'] = $this->referer;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->signToken) {
            $res['sign_token'] = $this->signToken;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetDownloadUrlRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['addition_data'])){
            $model->additionData = $map['addition_data'];
        }
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        if(isset($map['expire_sec'])){
            $model->expireSec = $map['expire_sec'];
        }
        if(isset($map['file_id'])){
            $model->fileId = $map['file_id'];
        }
        if(isset($map['file_id_path'])){
            $model->fileIdPath = $map['file_id_path'];
        }
        if(isset($map['file_name'])){
            $model->fileName = $map['file_name'];
        }
        if(isset($map['location'])){
            $model->location = $map['location'];
        }
        if(isset($map['referer'])){
            $model->referer = $map['referer'];
        }
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        if(isset($map['sign_token'])){
            $model->signToken = $map['sign_token'];
        }
        return $model;
    }
    /**
     * @description addition_data
     * @var mixed[]
     */
    public $additionData;

    /**
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

    /**
     * @description expire_sec
     * @example 15
     * @var int
     */
    public $expireSec;

    /**
     * @description file_id
     * @var string
     */
    public $fileId;

    /**
     * @var string
     */
    public $fileIdPath;

    /**
     * @description file_name
     * @example ccp.jpg
     * @var string
     */
    public $fileName;

    /**
     * @description location
     * @example cn-hangzhou
     * @var string
     */
    public $location;

    /**
     * @var string
     */
    public $referer;

    /**
     * @description share_id, either share_id or drive_id is required
     * @example 0018d25b-faed-4f5c-a67b-414e160b7953
     * @var string
     */
    public $shareId;

    /**
     * @var string
     */
    public $signToken;

}
