<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\PDS\SDK\Models\UploadPartInfo;

/**
 * 获取文件上传URL
 */
class BaseGetUploadUrlRequest extends Model {
    protected $_name = [
        'contentMd5' => 'content_md5',
        'driveId' => 'drive_id',
        'partInfoList' => 'part_info_list',
        'shareId' => 'share_id',
        'uploadId' => 'upload_id',
    ];
    public function validate() {
        Model::validateMaxLength('contentMd5', $this->contentMd5, 32);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validateRequired('uploadId', $this->uploadId, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->contentMd5) {
            $res['content_md5'] = $this->contentMd5;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->partInfoList) {
            $res['part_info_list'] = [];
            if(null !== $this->partInfoList && is_array($this->partInfoList)){
                $n = 0;
                foreach($this->partInfoList as $item){
                    $res['part_info_list'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->uploadId) {
            $res['upload_id'] = $this->uploadId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return BaseGetUploadUrlRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['content_md5'])){
            $model->contentMd5 = $map['content_md5'];
        }
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        if(isset($map['part_info_list'])){
            if(!empty($map['part_info_list'])){
                $model->partInfoList = [];
                $n = 0;
                foreach($map['part_info_list'] as $item) {
                    $model->partInfoList[$n++] = null !== $item ? UploadPartInfo::fromMap($item) : $item;
                }
            }
        }
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        if(isset($map['upload_id'])){
            $model->uploadId = $map['upload_id'];
        }
        return $model;
    }
    /**
     * @description content_md5
     * @example E10ADC3949BA59ABBE56E057F20F883E
     * @var string
     */
    public $contentMd5;

    /**
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

    /**
     * @description upload_part_list
     * @example 
     * @var UploadPartInfo[]
     */
    public $partInfoList;

    /**
     * @var string
     */
    public $shareId;

    /**
     * @description upload_id
     * @example 3920F2BE4D9446D6967E2ED505A97EFD
     * @var string
     */
    public $uploadId;

}
