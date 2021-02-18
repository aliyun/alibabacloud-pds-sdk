<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\PDS\SDK\Models\UploadPartInfo;

/**
 * create file request
 */
class HostingCreateFileRequest extends Model {
    protected $_name = [
        'additionData' => 'addition_data',
        'contentMd5' => 'content_md5',
        'contentType' => 'content_type',
        'driveId' => 'drive_id',
        'forbidOverwrite' => 'forbid_overwrite',
        'name' => 'name',
        'parentFilePath' => 'parent_file_path',
        'partInfoList' => 'part_info_list',
        'shareId' => 'share_id',
        'size' => 'size',
        'type' => 'type',
    ];
    protected $_default = [
        'forbidOverwrite' => 'false',
    ];
    public function validate() {
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validatePattern('shareId', $this->shareId, '[0-9a-zA-Z-]+');
        Model::validateRequired('name', $this->name, true);
        Model::validateRequired('parentFilePath', $this->parentFilePath, true);
        Model::validateRequired('type', $this->type, true);
        Model::validateMaxLength('name', $this->name, 1024);
        Model::validateMinLength('name', $this->name, 1);
        Model::validateMaximum('size', $this->size, 53687091200);
        Model::validateMinimum('size', $this->size, 0);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->contentMd5) {
            $res['content_md5'] = $this->contentMd5;
        }
        if (null !== $this->contentType) {
            $res['content_type'] = $this->contentType;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->forbidOverwrite) {
            $res['forbid_overwrite'] = $this->forbidOverwrite;
        }
        if (null !== $this->name) {
            $res['name'] = $this->name;
        }
        if (null !== $this->parentFilePath) {
            $res['parent_file_path'] = $this->parentFilePath;
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
        if (null !== $this->size) {
            $res['size'] = $this->size;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return HostingCreateFileRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['addition_data'])){
            $model->additionData = $map['addition_data'];
        }
        if(isset($map['content_md5'])){
            $model->contentMd5 = $map['content_md5'];
        }
        if(isset($map['content_type'])){
            $model->contentType = $map['content_type'];
        }
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        if(isset($map['forbid_overwrite'])){
            $model->forbidOverwrite = $map['forbid_overwrite'];
        }
        if(isset($map['name'])){
            $model->name = $map['name'];
        }
        if(isset($map['parent_file_path'])){
            $model->parentFilePath = $map['parent_file_path'];
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
        if(isset($map['size'])){
            $model->size = $map['size'];
        }
        if(isset($map['type'])){
            $model->type = $map['type'];
        }
        return $model;
    }
    /**
     * @description addition_data
     * @var mixed[]
     */
    public $additionData;

    /**
     * @description ContentMd5
     * @example E10ADC3949BA59ABBE56E057F20F883E
     * @var string
     */
    public $contentMd5;

    /**
     * @description ContentType
     * @example application/json
     * @var string
     */
    public $contentType;

    /**
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

    /**
     * @description forbid_overwrite
type: boolean
     * @var bool
     */
    public $forbidOverwrite;

    /**
     * @description Name
     * @example ccp.jpg
     * @var string
     */
    public $name;

    /**
     * @description parent_file_path
     * @var string
     */
    public $parentFilePath;

    /**
     * @description part_info_list
     * @var UploadPartInfo[]
     */
    public $partInfoList;

    /**
     * @description share_id
     * @var string
     */
    public $shareId;

    /**
     * @description Size
     * @var int
     */
    public $size;

    /**
     * @description Type
     * @example file
     * @var string
     */
    public $type;

}
